import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-purchase-workflow",
    description="Meta package for oca-purchase-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-procurement_batch_generator',
        'odoo14-addon-product_form_purchase_link',
        'odoo14-addon-purchase_cancel_reason',
        'odoo14-addon-purchase_commercial_partner',
        'odoo14-addon-purchase_delivery_split_date',
        'odoo14-addon-purchase_discount',
        'odoo14-addon-purchase_exception',
        'odoo14-addon-purchase_fop_shipping',
        'odoo14-addon-purchase_invoice_plan',
        'odoo14-addon-purchase_isolated_rfq',
        'odoo14-addon-purchase_last_price_info',
        'odoo14-addon-purchase_location_by_line',
        'odoo14-addon-purchase_manual_currency',
        'odoo14-addon-purchase_minimum_amount',
        'odoo14-addon-purchase_open_qty',
        'odoo14-addon-purchase_order_approval_block',
        'odoo14-addon-purchase_order_approved',
        'odoo14-addon-purchase_order_archive',
        'odoo14-addon-purchase_order_line_deep_sort',
        'odoo14-addon-purchase_order_line_menu',
        'odoo14-addon-purchase_order_line_packaging_qty',
        'odoo14-addon-purchase_order_line_price_history',
        'odoo14-addon-purchase_order_line_sequence',
        'odoo14-addon-purchase_order_secondary_unit',
        'odoo14-addon-purchase_order_type',
        'odoo14-addon-purchase_order_uninvoiced_amount',
        'odoo14-addon-purchase_product_usage',
        'odoo14-addon-purchase_propagate_qty',
        'odoo14-addon-purchase_quick',
        'odoo14-addon-purchase_reception_notify',
        'odoo14-addon-purchase_reception_status',
        'odoo14-addon-purchase_request',
        'odoo14-addon-purchase_request_cancel_confirm',
        'odoo14-addon-purchase_request_department',
        'odoo14-addon-purchase_request_tier_validation',
        'odoo14-addon-purchase_request_type',
        'odoo14-addon-purchase_requisition_tier_validation',
        'odoo14-addon-purchase_rfq_number',
        'odoo14-addon-purchase_security',
        'odoo14-addon-purchase_tier_validation',
        'odoo14-addon-purchase_work_acceptance',
        'odoo14-addon-purchase_work_acceptance_evaluation',
        'odoo14-addon-purchase_work_acceptance_invoice_plan',
        'odoo14-addon-purchase_work_acceptance_late_fines',
        'odoo14-addon-vendor_transport_lead_time',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
