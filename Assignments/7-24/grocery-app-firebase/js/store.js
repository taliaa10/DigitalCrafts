class Store {
    constructor(name, address) {
        this.name = name
        this.address = address
        this.storeId = ''
        this.groceryItems = []
    }

    addGroceryItem(groceryItem) {
        this.groceryItems.push(groceryItem)
    }
}