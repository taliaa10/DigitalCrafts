class Store {
    constructor(name, address) {
        this.name = name
        this.address = address
        this.storeId = ''
        this.groceryItems = []
    }

    deleteLocation(store) {
        console.log(store)
        // locationsRef.child(location).remove()
        
    }
}