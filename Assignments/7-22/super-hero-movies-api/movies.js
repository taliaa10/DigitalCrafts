let movieListDiv = document.getElementById('movie-list')
let movieDetailsDiv = document.getElementById('movie-details')
let movieListTitles = document.querySelectorAll('.movie-list__title')
let searchbox = document.getElementById('searchbox')

searchbox.focus()

document.addEventListener('keypress', (e) => {
    if (e.keyCode === 13 || e.which === 13) {
        searchbox.select().focus()
    }
})

searchbox.addEventListener('keypress', (e) => {
    if (e.keyCode === 13 || e.which === 13) {
        let searchboxValue = searchbox.value


        let moviesURL = `http://www.omdbapi.com/?s=${searchboxValue}&apikey=b0869d10`


        let req = new XMLHttpRequest()
        req.open('GET', moviesURL)
        req.addEventListener('load', () => {
            let movies = JSON.parse(event.currentTarget.responseText)

            let movieItems = movies.Search.map(movie => {
                return `<div>
                            
                            <button id=poster-button onclick = "showDetails('${movie.imdbID}')">
                             
                            <img src='${movie.Poster == "N/A" ? "placeholder.png" : movie.Poster}' class="movie-list__poster"/>
                            </button>
                    
                            <h2><button onclick = "showDetails('${movie.imdbID}')" class="movie-list__title">
                            ${movie.Title}
                            </button></h2>
                        </div>`
        
            
            })
        
            movieListDiv.innerHTML = movieItems.join('')
            
            searchbox.addEventListener('click', () => {
                searchbox.select()
            })


        })
        
        req.send()

    }
})

function showDetails(imdbid) {

    
    let movieDetailsURL = `http://www.omdbapi.com/?i=${imdbid}&apikey=b0869d10`

    let detailreq = new XMLHttpRequest()
    detailreq.open('GET', movieDetailsURL)
    detailreq.addEventListener('load', () => {
        let moviesDetails = JSON.parse(event.currentTarget.responseText)


        
        let movieDetails =
            `<div class='movie-details__stuff'>
                <h2 class='movie-details__title'>${moviesDetails.Title}</h2>
                <img src='${moviesDetails.Poster == "N/A" ? "placeholder.png" : moviesDetails.Poster}' class='movie-details-img'>
                <p>${moviesDetails.Plot}</p>
            </div>`

            movieDetailsDiv.innerHTML = movieDetails
            console.log(movieDetails)
    })

    detailreq.send()
}




// http://www.omdbapi.com/?t=batman

// http://www.omdbapi.com/?apikey=b0869d10&

// movie details URL
// http://www.omdbapi.com/?i=insertSelectedimdbIDhere&apikey=insertyourkeyhere 

// movie details example with my API
// http://www.omdbapi.com/?i=tt1877832&apikey=b0869d10

// movie details with specific movie
// http://www.omdbapi.com/?i=${movie.imdbID}&apikey=b0869d10

//  myAPIkey = b0869d10

// ${imdbID} for the imdbID


