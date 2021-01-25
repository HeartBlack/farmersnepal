function addToCart(productID) {
  fetch('/cart/add/' + productID).then(function (response) {
      return response.json()
  })
      .then(function (data) {
          alert('Product Added Succesfully');
          document.querySelector('#insertCartTotal').innerHTML = data.message
          
          
      })
      .then (function(data){
        document.querySelectorAll('.discount').innerHTML = data.discount 
    })
      
      
}
