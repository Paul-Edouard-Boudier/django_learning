/*
Use of 'attr' instead of 'data' because we do some dynamic modification of the attribute
When we use the 'data()' method it's beacuse we want the initial value of the object

data-product-id = the id of the cannedfood
                (use to target the good button to add to our cart)

data-stock-id = the id of the stock
                (use to know which one of the 'version' of the canned food the user wants
            eg: 250g or 500g so on...)
*/


let add_to_cart_selector = '.btn-add-to-cart',
        quantity_infos_selector = '.quantity-left',
        format_selector = '.select-format',
        notification_success_selector = '#notification-success',
        notification_error_selector = '#notification-error';

// try to add element clicked to the cart
$(add_to_cart_selector).on('click', function(e) {
    e.preventDefault();
    let url = $(this).attr('data-url');
    add_to_cart(url);
})

// change the quantity displayed and url associated with the new format selected
$(format_selector).on('change', function() {
    let stock_id_selected = $(this).find('option:selected').data('stock-id'),
        product_id = $(this).data('product-id');
    display_quantity(stock_id_selected);
    change_add_to_cart_url(product_id, stock_id_selected);
})


// ----------------------------------------------------------------------------
//                              FUNCTIONS
// ----------------------------------------------------------------------------

/**
 * Change an element of the notification and display it for a definite amount
 * of time
 */
function display_notification_success(message) {
    let notification = $(notification_success_selector);
    display_notification(notification, message)
}


function display_notification_error(message) {
    let notification = $(notification_error_selector);
    display_notification(notification, message)
}

function display_notification(notification, message) {
    notification.find('#text-to-replace').text(message);
    notification.show();
    setTimeout(function() {
        notification.fadeOut('slow')
    }, 2500);
}


/**
 * Display the div that holds the quantity relativ to the object
 * targeted by the select
 */
function display_quantity(id) {
    $(quantity_infos_selector).each(function() {
        if ($(this).data('qty-id') == id) {
            $(this).show();
        } else {
            $(this).hide();
        }
    });
}


/**
 * change the data('url') of the button, used to know what url to call in ajax
 * we use 'data()' here because we won't change the attr and so that
 * we kinda avoid the user that messes with the DOM
 */
function change_add_to_cart_url(product_id, new_stock_id) {
    /**
     * regex takes first part of a url-like string
     * it captures something like that : '/word/other_word/12'
     * and the group take the first part of the string : '/word/other_word'
     * Used to change the number of the url to target antoher element_id
     */
    let regex = /((?:\/|\w)*)\/[0-9]+$/,
        old_url = $(add_to_cart_selector).attr('data-url'),
        matches = old_url.match(regex);
    if (matches) {
        new_url = matches[1] + '/' + new_stock_id
    }
    // target the good add_to_cart button and change it's url
    $(add_to_cart_selector+"[data-product-id='"+product_id+"']").attr('data-url', new_url)
}


// -------------------------------
//              AJAX
// -------------------------------
/**
 * AJAX Call to update the cart
 */
function add_to_cart(url) {
    $.get(url).done(function(data) {
        display_notification_success(data.name)
    }).fail(function() {
        display_notification_error('une erreur est survenue');
    })
}
