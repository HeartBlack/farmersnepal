function addToCart(productID) {
  fetch('/cart/add/' + productID).then(function (response) {
      return response.json()
  })
      .then(function (data) {
          alert('Product Added Succesfully');
          document.querySelector('#insertCartTotal').innerHTML = data.message
          
          
      })
     
      
}
