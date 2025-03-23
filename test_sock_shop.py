import pytest
from app import app, get_available_products, get_product_by_id, get_all_categories

# Set up testing configuration
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False

# Original tests from Part 1
def test_get_available_products():
    """Test product retrieval functionality"""
    products = get_available_products()
    assert len(products) == 3
    assert all('id' in p and 'name' in p and 'description' in p and 
              'base_price' in p and 'image' in p and 'category' in p 
              for p in products)
    assert len(get_available_products('funny')) == 2

def test_get_product_by_id():
    """Test product lookup by ID"""
    product = get_product_by_id(1)
    assert product and product['id'] == 1 and product['name'] == 'Meme Lord'
    assert get_product_by_id(999) is None

def test_get_all_categories():
    """Test category retrieval"""
    categories = get_all_categories()
    assert len(categories) == 2
    assert 'funny' in categories and 'school' in categories

# Simple tests for Part 2
def test_empty_cart_checkout_redirect():
    """Test that users with empty carts are redirected from checkout"""
    with app.test_client() as client:
        # Set up an empty cart in the session
        with client.session_transaction() as session:
            session['cart'] = []
        
        # Try to access checkout page
        response = client.get('/checkout', follow_redirects=True)
        
        # Should redirect to home page
        assert response.request.path == '/'

def test_cart_with_items():
    """Test that cart page displays correctly with items"""
    with app.test_client() as client:
        # Set up a cart with an item
        with client.session_transaction() as session:
            session['cart'] = [{
                'product_id': 1,
                'name': 'Test Sock',
                'price': 10.99,
                'quantity': 2,
                'custom_text': 'Test',
                'total': 21.98
            }]
        
        # Access cart page
        response = client.get('/cart')
        
        # Check cart page loads and shows the item
        assert response.status_code == 200
        assert b'Test Sock' in response.data
        assert b'21.98' in response.data