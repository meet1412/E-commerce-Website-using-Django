var updateBtns = document.getElementsByClassName('update-cart');

// Attach click event listeners to all update buttons
for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product; // Extract product ID
        var action = this.dataset.action;     // Extract action (add/remove)
        console.log('productId:', productId, 'Action:', action);

        // Determine if the user is logged in or a guest
        console.log('USER:', user);
        if (user === 'AnonymousUser') {
            addCookieItem(productId, action); // Handle cart for guest users
        } else {
            updateUserOrder(productId, action); // Handle cart for authenticated users
        }
    });
}

// Function to update the cart for authenticated users
function updateUserOrder(productId, action) {
    console.log('User is authenticated, sending data...');

    var url = '/update_item/'; // Endpoint for updating the cart

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken, // Include CSRF token for security
        },
        body: JSON.stringify({ productId: productId, action: action }) // Send data as JSON
    })
        .then((response) => response.json())
        .then((data) => {
            console.log('Data:', data);
            location.reload(); // Reload the page to reflect changes
        })
        .catch((error) => {
            console.error('Error updating cart for authenticated user:', error);
        });
}

// Function to handle cart updates for guest users
function addCookieItem(productId, action) {
    console.log('User is not authenticated');

    // Add item to the cart
    if (action === 'add') {
        if (cart[productId] === undefined) {
            cart[productId] = { quantity: 1 }; // Add product with quantity 1 if not in cart
        } else {
            cart[productId]['quantity'] += 1; // Increment quantity if product exists
        }
    }

    // Remove item from the cart
    if (action === 'remove') {
        cart[productId]['quantity'] -= 1; // Decrement quantity
        if (cart[productId]['quantity'] <= 0) {
            console.log('Item should be deleted');
            delete cart[productId]; // Remove product if quantity is 0 or less
        }
    }

    console.log('Updated CART:', cart);

    // Update the cart in cookies
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';

    // Reload the page to show the updated cart
    location.reload();
}
