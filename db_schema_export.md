## Table: account_win_tmp
- **customer_code**: varchar(50), primary key
- **email**: varchar(100)

## Table: app_map_factory
- **factory_id**: int
- **customer_code**: nvarchar(50)

## Table: app_mappc
- **product_code**: nvarchar(50)
- **category_id**: int

## Table: app_user
- **customer_code**: nvarchar(50)
- **org_code**: nvarchar(50)

## Table: category_products
- **id**: int, primary key
- **category_id**: int, foreign key → tb_category(id)
- **product_id**: int, foreign key → tb_product(id)
- **created_at**: datetime
- **created_by**: int
- **updated_at**: datetime
- **updated_by**: int
- **Indexes**:
  - `UQ_CategoryProduct` on (category_id, product_id)

## Table: product_brand
- **product_id**: int, primary key
- **brand**: nvarchar(50), primary key

## Table: product_brand_tmp
- **column1**: nvarchar(50)
- **column2**: nvarchar(50)

## Table: role_permision
- **id**: int, primary key
- **role_id**: int
- **permision_id**: int

## Table: sysdiagrams
- **name**: nvarchar(128)
- **principal_id**: int
- **diagram_id**: int, primary key
- **version**: int
- **definition**: varbinary(-1)
- **Indexes**:
  - `UK_principal_name` on (principal_id, name)

## Table: tb_admin_factory
- **id**: int, primary key
- **user_id**: int
- **factory_id**: int
- **active**: bit
- **created_at**: datetime
- **Indexes**:
  - `UQ__tb_admin__B9BE370EA4E1E32C` on (user_id)

## Table: tb_api_keys
- **id**: uniqueidentifier, primary key
- **key_hash**: nvarchar(255)
- **label**: nvarchar(500)
- **scope**: nvarchar(-1)
- **created_at**: datetime2
- **expires_at**: datetime2
- **revoked**: bit
- **daily_quota**: int
- **Indexes**:
  - `UQ__tb_api_k__14E22E86E0741108` on (key_hash)

## Table: tb_blacklisted_tokens
- **id**: int, primary key
- **token**: varchar(500)
- **created_at**: datetime
- **Indexes**:
  - `UQ_BlacklistedTokens_Token` on (token)
  - `IX_BlacklistedTokens_Token` on (token)

## Table: tb_brand
- **id**: int, primary key
- **brand_name**: nvarchar(50)

## Table: tb_business
- **id**: int, primary key
- **business_name**: nvarchar(250)
- **secrect_code**: nvarchar(250)

## Table: tb_category
- **id**: int, primary key
- **category_code**: nvarchar(50)
- **category_name**: nvarchar(255)
- **business_id**: int, foreign key → tb_business(id)
- **parent_id**: int, foreign key → tb_category(id)
- **order_number**: int
- **active**: bit
- **created_at**: datetime
- **updated_at**: datetime
- **Indexes**:
  - `UQ_Category_Code_Business` on (category_code, business_id)

## Table: tb_channel
- **id**: int, primary key
- **channel_code**: nvarchar(50)
- **channel_name**: nvarchar(255)
- **business_id**: int, foreign key → tb_business(id)
- **active**: bit
- **created_at**: datetime
- **updated_at**: datetime
- **Indexes**:
  - `UQ_Channel_Code_Business` on (channel_code, business_id)

## Table: tb_customer
- **id**: int, primary key
- **customer_code**: nvarchar(50)
- **customer_name**: nvarchar(350)
- **business_id**: int, foreign key → tb_business(id)
- **active**: bit
- **created_at**: datetime
- **updated_at**: datetime
- **Indexes**:
  - `UQ_Customer_Code` on (customer_code)

## Table: tb_factory
- **id**: int, primary key
- **factory_name**: nvarchar(255)
- **business_id**: int, foreign key → tb_business(id)
- **org_code**: nvarchar(50)

## Table: tb_lang
- **id**: int, primary key
- **language_code**: nvarchar(50)
- **key_name**: nvarchar(50)
- **translation**: nvarchar(150)

## Table: tb_navigation_menu
- **menu_id**: int, primary key
- **title**: nvarchar(100)
- **url**: nvarchar(255)
- **icon**: nvarchar(50)
- **parent_id**: int
- **display_order**: int
- **is_active**: bit
- **created_at**: datetime
- **updated_at**: datetime

## Table: tb_order
- **id**: int, primary key
- **po_doc_no**: int
- **created_by**: int, foreign key → tb_users(id)
- **order_date**: datetime
- **address**: nvarchar(500)
- **car_number**: nvarchar(50)
- **org_code**: varchar(50)
- **delivery_date**: date
- **customer_code**: varchar(50)
- **status**: varchar(20)
- **is_sync**: bit
- **ord_doc_no**: nvarchar(50)
- **is_check**: bit
- **is_restore**: bit
- **is_special**: char(1)

## Table: tb_orderdetail
- **id**: int, primary key
- **order_id**: int, foreign key → tb_order(id)
- **product_id**: int, foreign key → tb_product(id)
- **price**: decimal
- **quantity**: int
- **item_weight**: int
- **product_code**: nvarchar(50)
- **remark**: nvarchar(-1)
- **product_brandcode**: nchar(10)
- **packsize_code**: int
- **out_of_stock**: nchar(10)
- **attribute_name**: nvarchar(100)

## Table: tb_permisions
- **id**: int, primary key
- **name**: nvarchar(250)
- **resource**: nvarchar(50)
- **action**: nvarchar(50)
- **method**: nvarchar(50)
- **created_at**: datetime

## Table: tb_price
- **id**: int
- **org_code**: nvarchar(50), primary key
- **product_code**: nvarchar(50), primary key
- **class_price**: nvarchar(50), primary key
- **price**: float

## Table: tb_product
- **id**: int, primary key
- **product_code**: nvarchar(50)
- **product_name**: nvarchar(150)
- **name_eng**: nvarchar(50)
- **unit_name**: nvarchar(50)
- **package_size**: int
- **active**: bit
- **image**: nvarchar(100)
- **brand_code**: nvarchar(50)
- **item_weight**: float
- **product_brandcode**: nvarchar(50)
- **Indexes**:
  - `Index_tb_product_1` on (product_code)

## Table: tb_product_category
- **id**: int, primary key
- **product_code**: nvarchar(50)
- **category_id**: int
- **business_id**: int
- **created_at**: datetime
- **created_by**: int
- **Indexes**:
  - `IX_tb_product_category` on (product_code, category_id)

## Table: tb_product_plan
- **id**: int, primary key
- **plan_date**: date
- **product_code**: nvarchar(50)
- **plan_quantity**: int
- **created_date**: date
- **created_by**: int
- **org_code**: nvarchar(50)
- **plan_weight**: int
- **Indexes**:
  - `Index_tb_product_plan_1` on (plan_date, org_code, product_code)

## Table: tb_product_type
- **id**: int, primary key
- **type_code**: nvarchar(50)
- **type_name**: nvarchar(255)
- **business_id**: int, foreign key → tb_business(id)
- **order_number**: int
- **active**: bit
- **created_at**: datetime
- **updated_at**: datetime
- **Indexes**:
  - `UQ_ProductType_Code_Business` on (type_code, business_id)

## Table: tb_product_type_mapping
- **id**: int, primary key
- **product_code**: nvarchar(50)
- **type_id**: int, foreign key → tb_product_type(id)
- **business_id**: int, foreign key → tb_business(id)
- **created_at**: datetime
- **created_by**: nvarchar(50)
- **Indexes**:
  - `UQ_Product_Type_Business` on (product_code, type_id, business_id)

## Table: tb_role_menu
- **role_id**: int, primary key, foreign key → tb_roles(id)
- **menu_id**: int, primary key, foreign key → tb_navigation_menu(menu_id)
- **business_id**: int, primary key, foreign key → tb_business(id)

## Table: tb_roles
- **id**: int, primary key
- **name**: nvarchar(50)
- **description**: nvarchar(250)
- **parent**: int
- **business_id**: int
- **updated_at**: datetime

## Table: tb_stock
- **id**: int, primary key
- **product_code**: nvarchar(50)
- **org_code**: nvarchar(50)
- **stock_quantity**: int
- **Indexes**:
  - `IX_tb_stock` on (org_code, product_code)

## Table: tb_test
- **name**: nvarchar(50)
- **description**: nvarchar(50)

## Table: tb_tests
- **id**: int, primary key
- **name**: nvarchar(50)

## Table: tb_tmp
- **username**: nvarchar(100)
- **brand**: nvarchar(50)

## Table: tb_user_business
- **id**: int, primary key
- **user_id**: int
- **business_id**: int
- **created_at**: datetime
- **created_by**: int
- **active**: bit
- **Indexes**:
  - `Index_tb_user_business_1` on (business_id, user_id)

## Table: tb_user_classprice
- **customer_code**: nvarchar(50), primary key
- **org_code**: nvarchar(50), primary key
- **class_price**: nvarchar(50), primary key
- **id**: int

## Table: tb_user_factory
- **id**: int, primary key
- **user_id**: int
- **factory_id**: int
- **active**: bit
- **created_at**: datetime

## Table: tb_user_menu
- **user_menu_id**: int, primary key
- **user_id**: int, foreign key → tb_users(id)
- **menu_id**: int, foreign key → tb_navigation_menu(menu_id)
- **can_access**: bit
- **arrange**: int

## Table: tb_users
- **id**: int, primary key
- **customer_code**: nvarchar(50)
- **fullname**: nvarchar(100)
- **username**: nvarchar(100)
- **password**: nvarchar(350)
- **phone**: nvarchar(50)
- **active**: bit
- **created_by**: int
- **created_at**: datetime
- **is_delete**: bit
- **address**: nvarchar(150)
- **updated_at**: datetime
- **brand**: nvarchar(50)
- **Indexes**:
  - `IX_tb_users` on (username, customer_code, is_delete)

## Table: tb_variants
- **id**: int, primary key
- **product_id**: int
- **attribute_name**: nvarchar(100)

## Table: user_brand_tmp
- **ID**: smallint
- **Brand**: nvarchar(50)

## Table: user_roles
- **id**: int, primary key
- **user_id**: int
- **role_id**: int

## Table: vo.hieu
- **id**: nchar(10)

## Stored Procedures
- get_user
- ps_test
- get_test
- ps_caculator
- sp_upgraddiagrams
- sp_helpdiagrams
- sp_helpdiagramdefinition
- sp_creatediagram
- sp_renamediagram
- sp_alterdiagram
- sp_dropdiagram
