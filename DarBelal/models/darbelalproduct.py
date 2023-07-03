from odoo import api, models, fields


class ProductType(models.Model):
    _name = "darbelal.productproperties"
    name = fields.Char(string="Type", translate=True)


class ProductVolume(models.Model):
    _name = "darbelal.productvolume"
    name = fields.Char(string="Volume", translate=True)


class ProductBrand(models.Model):
    _name = "darbelal.productbrand"
    name = fields.Char(string="Brand", translate=True)


class ProductManufacturer(models.Model):
    _name = "darbelal.productmanufacturer"
    name = fields.Char(string="Manufacturer", translate=True)


class ProductMadeIn(models.Model):
    _name = "darbelal.productmadein"
    name = fields.Char(string="Product Group", translate=True)


class ProductCategory(models.Model):
    _name = "darbelal.productcategory"
    name = fields.Char(string="Category", translate=True)


class ProductPriseCategory(models.Model):
    _name = "darbelal.productprisecategory"
    name = fields.Char(string="Prise Category", translate=True)


class ProductBrandOwner(models.Model):
    _name = "darbelal.productbrandowner"
    name = fields.Char(string="Exporting Company", translate=True)


class ProductSubCategory(models.Model):
    _name = "darbelal.productsubcategory"
    name = fields.Char(string="Sub Category", translate=True)


class ProductFragrancFor(models.Model):
    _name = "darbelal.productfragrancfor"
    name = fields.Char(string="Fragranc For", translate=True)


class ProductImportCompany(models.Model):
    _name = "darbelal.productimportcompany"
    name = fields.Char(string="Import Company", translate=True)


class ProductSubBrand(models.Model):
    _name = "darbelal.productsubbrand"
    name = fields.Char(string="Sub Brand", translate=True)


class ProductProduct(models.Model):
    _inherit = "product.template"

    x_fragrance_type = fields.Many2one("darbelal.productproperties", string="Fragrance Type")
    x_Volume = fields.Many2one("darbelal.productvolume", string="Product Volume")
    # x_x_Volume=fields.Char(string="Volume",compute="compute_Volume")
    # def compute_Volume(self):
    #     self.x_x_Volume=self.x_Volume.name


    x_Brand = fields.Many2one("darbelal.productbrand", string="Brand")

    x_manufacturer = fields.Many2one(
        "darbelal.productmanufacturer", string="Manufacturer"
    )

    x_exporting_company = fields.Many2one(
        "darbelal.productbrandowner", string="Exporting Company"
    )
    x_import_company = fields.Many2one(
        "darbelal.productimportcompany", string="Importing Company"
    )

    x_product_group = fields.Many2one("darbelal.productmadein", string="Product Group")

    x_generate_name = fields.Many2one("darbelal.generatename", string="Generate Name")

    x_generate_name_ = fields.Char(
        string="name ProductId", compute="compute_generate_name"
    )
    x_description = fields.Text(string="Description")

    @api.depends(
        "x_Brand", "x_Volume", "x_Brand", "name", "x_description", "x_generate_name"
    )
    def compute_generate_name(self):
        x = str(self.x_generate_name.name)
        # y = str(self.x_Type.name)
        z = str(self.x_Volume.name)
        m = str(self.x_Brand.name)
        n = str(self.name)
        c = str(self.x_category.name)

        self.x_generate_name_ = x.replace("volume", z)
        # self.x_generate_name_ = x.replace("type", y)
        self.x_generate_name_ = x.replace("name", n)
        self.x_generate_name_ = x.replace("brand", m)
        self.x_generate_name_ = x.replace("category", c)
        # self.x_generate_name_ = str(self.x_generate_name_) + str(self.x_description)

        print(c)

    x_sub_brand = fields.Many2one("darbelal.productsubbrand", string="Sub Brand")


    x_product_class = fields.Many2one("darbelal.productcategory", string="Product Class")

    x_Product_sub_class = fields.Many2one(
        "darbelal.productsubcategory", string="Product Sub-Class"
    )

    x_fragranc_for = fields.Many2one(
        "darbelal.productfragrancfor", string="For"
    )
    x_similar_int_brand=fields.Char(string='Similar Int. Brand')
        
    x_product_segmentation = fields.Many2one(
        "darbelal.productprisecategory", string="Product Segmentation"
    )

    x_retail_ratio = fields.Float(String="Retail Ratio")
    x_min_selling_price = fields.Float(
        string="Min Selling Price", compute="compute_min_selling_price",
    )

    @api.depends("x_retail_ratio", "list_price")
    def compute_min_selling_price(self):
        self.x_min_selling_price = (self.list_price * self.x_retail_ratio) / 100



    x_x_x=fields.Char(string="x_x_x",compute="compute_x_x")


    @api.depends(
        "x_description",'x_sub_brand',
        "x_Brand","x_product_class",
        "x_Product_sub_class","x_fragranc_for",
        "x_fragrance_type","x_Volume",
        "country_of_origin","product_tag_ids",
        
        )
    @api.onchange(
        "x_description",'x_sub_brand',
        "x_Brand","x_product_class","x_Product_sub_class",
        "x_fragranc_for","x_fragrance_type","x_Volume",
        "country_of_origin","product_tag_ids",
        )
    def compute_x_x(self):
        m=self.x_description
        self.x_x_x=f" \
            Class:{self.x_product_class.name}\n\
            Sub-Class:{self.x_Product_sub_class.name} \n\
            Brand:{self.x_Brand.name}\n\
            sub Brand:{self.x_sub_brand.name}\n\
            Product Group:{self.x_product_group.name}\n\
            Fragrance for:{self.x_fragranc_for.name} \n\
            Fragrance type:{self.x_fragrance_type.name}\n \
            Volume:{self.x_Volume.name} \n\
            Made In:{self.country_of_origin.name}\n\
            Description & notes:{self.x_description}"

    @api.onchange(
        'x_sub_brand',
        "x_Brand","x_category","x_sub_category",
        "x_fragranc_for","x_Type","x_Volume",
        "country_of_origin","product_tag_ids",
        "x_description"
        
        )
    @api.depends(
        'x_sub_brand',"description_sale",
        "x_Brand","x_category",
        "x_sub_category","x_fragranc_for",
        "x_Type","x_Volume",
        "country_of_origin","product_tag_ids",
        "x_description"
        )
    def description(self):
        self.description_sale=self.x_x_x

        print("eldoza",self.x_x_x)
        
        



class CustomerType(models.Model):
    _name = "darbelal.customertype"
    name = fields.Char(string="client_type")
    discount = fields.Float(string="discount percentage")


class GenerateName(models.Model):
    _name = "darbelal.generatename"
    name = fields.Char(string="Generate Name")


class ResPartner(models.Model):
    _inherit = "res.partner"

    x_type_client = fields.Many2one("darbelal.customertype", string="client type")
    x_discount = fields.Float(
        related="x_type_client.discount", string="discount percentage"
    )


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_type_client = fields.Many2one(
        related="partner_id.x_type_client", string="client type"
    )
    x_discount = fields.Float(related="partner_id.x_discount", string="discount")


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    x_type_client = fields.Many2one(
        related="order_partner_id.x_type_client", string="client type"
    )
    discount_customer = fields.Float(
        related="order_partner_id.x_discount", string="discount"
    )
    price = fields.Float(related="product_id.list_price", string="price")
    x_min_selling_price = fields.Float(
        related="product_id.x_min_selling_price", string="price"
    )

    @api.onchange("price_unit", "discount_customer", "x_min_selling_price", "price")
    def _onchange_partner_id(self):
        self.price_unit = (
            self.price
            - (self.price - self.x_min_selling_price) * self.discount_customer / 100
        )


