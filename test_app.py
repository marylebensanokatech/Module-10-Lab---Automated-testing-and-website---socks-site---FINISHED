from app import get_available_products, get_product_by_id, get_all_categories

def test_get_available_products():
    """
    This test verifies our product retrieval functionality:
    - Checks that we have the correct number of products (3)
    - Ensures each product contains all required data fields
    - Tests that category filtering works correctly (2 'funny' products)
    
    If this test fails, it could mean:
    - Products are missing from the database
    - Products are missing required fields
    - The category filtering logic is broken
    """
    products = get_available_products()
    assert len(products) == 3
    assert all('id' in p and 'name' in p and 'description' in p and 
              'base_price' in p and 'image' in p and 'category' in p 
              for p in products)
    assert len(get_available_products('funny')) == 2

def test_get_product_by_id():
    """
    This test checks our product lookup functionality:
    - Verifies we can retrieve a product using its ID
    - Confirms the product data is correct
    - Tests that invalid IDs return None instead of causing errors
    
    If this test fails, it could mean:
    - The product with ID 1 is missing or has incorrect data
    - The function isn't handling invalid IDs properly
    """
    product = get_product_by_id(1)
    assert product and product['id'] == 1 and product['name'] == 'Meme Lord'
    assert get_product_by_id(999) is None

def test_get_all_categories():
    """
    This test examines our category management:
    - Checks that we have the expected number of categories (2)
    - Verifies that all expected categories exist ('funny' and 'school')
    
    If this test fails, it could mean:
    - Categories are missing from the database
    - The category retrieval logic is broken
    """
    categories = get_all_categories()
    assert len(categories) == 2
    assert 'funny' in categories and 'school' in categories