$('.ui.labeled.icon.sidebar')
  .sidebar('toggle')
;

$('.ui.accordion')
  .accordion()
;

$('.ui.sticky')
  .sticky({
      context: '#product-card',
      pushing: true
  })
;

$('.ui.rating')
  .rating()
;


let addStoreTextbox = document.getElementById('store-name-textbox')
let addAddressTextbox = document.getElementById('store-address-textbox')
let displayStoresDiv = document.getElementById('display-stores-div')
let storeAccordion = document.getElementById('store-accordion')
let groceryItemTextbox = document.getElementById('grocery-item-textbox')
let groceryCategoryTextbox = document.getElementById('grocery-category-textbox')
let addStoreBtn = document.getElementById('add-store-btn')


let storesRef = database.ref('stores')

storesRef.on('value',(snapshot) => {
    let stores = []

    for(key in snapshot.val()) {
        let user =snapshot.val()[key]
        user.key = key
        stores.push(user)
    }
    displayStores(stores)
})





// EVENT LISTENERS


addAddressTextbox.addEventListener('keypress', e => {
    if (e.keyCode === 13 || e.which === 13) {
        let addStoreTextboxValue = toTitleCase(addStoreTextbox.value)
        let addAddressTextboxValue = toTitleCase(addAddressTextbox.value)
        addStore(addStoreTextboxValue, addAddressTextboxValue)
        addStoreTextbox.value = ""
        addAddressTextbox.value = ""
        addStoreTextbox.focus()
    }
})


if (addStoreTextbox.value == ''){
addStoreTextbox.addEventListener('keypress', e => {
    if (e.keyCode === 13 || e.which === 13) {
        addAddressTextbox.focus()
    }
})
}

addStoreBtn.addEventListener('click', () => {
    let addStoreTextboxValue = toTitleCase(addStoreTextbox.value)
    let addAddressTextboxValue = toTitleCase(addAddressTextbox.value)
    addStore(addStoreTextboxValue, addAddressTextboxValue)
    addStoreTextbox.value = ""
    addAddressTextbox.value = ""
    addStoreTextbox.focus()
})


// if (groceryCategoryTextbox.value !== '') {
//     groceryCategoryTextbox.addEventListener('keypress', e => {
//         addGroceryItem(address)
//     })
// }




function addStore(store, address) {
    storesRef.push({
        name: store,
        address: address
    })
}





function displayStores(stores) {
    let storeItems = stores.map(store => {
        return `<div class="title store-title active">
        <i class="dropdown icon"></i>
        ${store.name} - ${store.address}
        <button class="ui icon button" style="float: right;" onclick='deleteStore("${store.key}")'><i class="trash icon"></i></button>
      </div>
      <div class="content">

                           
      </p>
<div class="ui middle aligned selection list animated">
      <div class="item">
        
        <div class="content">

        <div class="ui checkbox">
  <input type="checkbox" name="example">
  <label><div class="header">Bread - Food</div></label>
</div>
          
        </div>
      </div>
      <div class="item">
        <div class="content">
        
        <div class="ui checkbox">
  <input type="checkbox" name="example">
  <label><div class="header">Diaper - Baby</div></label>
</div>

        </div>
      </div>
      <div class="item">
        <div class="content">

        <div class="ui checkbox">
        <input type="checkbox" name="example">
        <label><div class="header">Soap - Health & Beauty</div></label>
      </div>
      

        </div>
      </div>

      <div class="ui input">

      <input type="text" class="grocery-textboxes" id="grocery-item-textbox" placeholder="Grocery Item...">

      <div class="ui action input">
      <input type="text" class="grocery-textboxes" id="grocery-category-textbox" placeholder="Category...">
      
      <button onclick='addGroceryItem("${store.address}")' class="ui icon button teal"><i class="plus square icon"></i></button>
      </div>   
      </div> 
    </div>
</div>`
                
    })
    storeAccordion.innerHTML = storeItems.join('')
}



function deleteStore(key) {
    storesRef.child(key).remove()

}


function addGroceryItem(address) {
    console.log(address)
    let groceriesRef = database.ref('stores').child('-Lkgy6Jx0mnefprfGufk').set({
        groceryName: 'bread',
        categoryName: 'food'
    })
    // console.log(groceriesRef)
}







function toTitleCase(str)  {
    return str.replace(
        /\w\S*/g,
        function(txt) {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
        }
    );
}



// exports.sendWelcomeEmail = functions.auth.user().onCreate((user) => {
    
//     const email = user.email
//     console.log(email)

//   });