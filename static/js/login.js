var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        console.log('productId:', productId, 'action:', action)
        console.log('USER:', user)


        updateUserOrder(productId, action)
    })
} 



function addCookieItem(productId, action){

    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }else{
            cart[productId]['quantity'] += 1
        }
    }


    if(action == 'remove'){
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity'] <= 0){
            console.log('Remove Item')
            delete cart[productId]
        }else{
            cart[productId]['quantity'] += 1
        }
    }

    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"



}




function updateUserOrder(productId, action){
    console.log('User is logged in Sending data...')


    var url = '/update_item/'

    const request = new Request(
        url,
        {
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            mode: 'same-origin', // Do not send CSRF token to another domain.
            body: JSON.stringify({'productId': productId, 'action':action}),
        }
       
    );

    fetch(request)

    .then((response) =>{
        return response.json()
        
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })

}
