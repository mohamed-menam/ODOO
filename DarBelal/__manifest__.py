# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "DarBelal",
    "version": "1.1",
    "summary": "MY First Model",
    "author": "QuadroZona",
    "sequence": 1,
    "description": """DarBelal""",
    "category": "Invoicing Management",
    "website": "https://www.odoo.com/page/billing",
    "license": "LGPL-3",
    "depends": [
        "sale_management",
        "sale_discount_total",
        "account",
        "l10n_generic_coa",
        "website",
        'website_sale',
        'hr'
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/customer_type.xml",
        "views/ProductProperties.xml",
        "views/productedite.xml",
        "views/productvolume.xml",
        "views/productbrand.xml",
        "views/productmanufacturer.xml",
        "views/respartener_type.xml",
        "views/saleordertype.xml",
        "views/product_made_in.xml",
        "views/product_category.xml",
        "views/product_prise_category.xml",
        "views/productbrandowner.xml",
        "views/product_sub_category.xml",
        "views/product_fragranc_for.xml",
        "views/product_sub_brand.xml",
        "views/productbrandowner.xml",
        # "views/generatename.xml",
        "views/product_import_company.xml",
        "views/employee.xml"
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
