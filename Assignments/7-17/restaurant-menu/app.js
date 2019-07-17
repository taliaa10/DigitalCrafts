let startersSection = document.getElementById("starters-section")
let entreesSection = document.getElementById("entrees-section")
let dessertsSection = document.getElementById("desserts-section")

let dishItems = document.getElementById("dish-items")

// STARTERS
let starterSection = dishes.filter(dish => {
    return dish.course == "Starters";
}).map(dish => {
    let starterDiv = `
    <div class="dish-item">
        <img src="${dish.imageURL}" alt="food-img">
        <div class="food-description">
            <h4>${dish.title}</h4>
            <span class="dish-description">${dish.description} ${dish.course}</span>
        </div>
        <span class="price">${dish.price}</span>
    </div>`

    return starterDiv
})

startersSection.innerHTML = starterSection.join('')

// ENTREES
let entreeSection = dishes.filter(dish => {
    return dish.course == "Entrees";
}).map(dish => {
    let entreeDiv = `
    <div class="dish-item">
        <img src="${dish.imageURL}" alt="food-img">
        <div class="food-description">
            <h4>${dish.title}</h4>
            <span class="dish-description">${dish.description} ${dish.course}</span>
        </div>
        <span class="price">${dish.price}</span>
    </div>`

    return entreeDiv
})

entreesSection.innerHTML = entreeSection.join('')

// DESSERTS
let dessertSection = dishes.filter(dish => {
    return dish.course == "Desserts";
}).map(dish => {
    let dessertDiv = `
    <div class="dish-item">
        <img src="${dish.imageURL}" alt="food-img">
        <div class="food-description">
            <h4>${dish.title}</h4>
            <span class="dish-description">${dish.description}</span>
        </div>
        <span class="price">${dish.price}</span>
    </div>`

    return dessertDiv
})

dessertsSection.innerHTML = dessertSection.join('') 




// let searchDropdown = document.getElementById("search-dropdown")

// searchDropdown.addEventListener('change', () => {
//     let filteredDishes = dishes.filter(dish => dish.course === searchDropdown.value)
//     console.log("loading starters")

//     return filteredDishes
    
//     dishItems.innerHTML = filteredDishes.join('')
// })

// dishItems.innerHTML = filteredDishes.join('')