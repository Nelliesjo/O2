const form = document.querySelector("form");

const input = document.querySelector("#query");


form.addEventListener("submit", async function (event) {
    event.preventDefault();


    const search = input.value;
    const url = `https://api.tvmaze.com/search/shows?q=${search}`;


    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
    } catch (fail) {
        console.error("Error:", fail);
    }
});