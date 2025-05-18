const form = document.querySelector("form");

const input = document.querySelector("#query");


form.addEventListener("submit", async function (event) {
    event.preventDefault();
    document.getElementById("results").innerHTML = ""

    const search = input.value;
    const url = `https://api.tvmaze.com/search/shows?q=${search}`;


    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log(data)
        for (let i = 0; i<data.length;i++){
        let name = data[i].show.name
        let page = data[i].show.url
        let sum = data[i].show.summary
        const createcount = document.getElementById("results")
        const cel = document.createElement("article")
        const page_n = document.createElement("h2")
        const link = document.createElement("a")
        const image = document.createElement("img")
        const summary = document.createElement("div")

        cel.appendChild(page_n)
        cel.appendChild(image)
        cel.appendChild(summary)
        cel.appendChild(link)

        page_n.innerHTML = `<h2>${name}</h2>`;
        link.innerHTML = `<a href="${page}" target="_blank">${page}</a>`
        if (data[0].show.image) {
        image.src = data[i].show.image.medium;
        image.alt = `${name}`;
        }
        summary.innerHTML = `<div>${sum}</div>`

        createcount.appendChild(cel);
        }

    } catch (error) {
        console.error("Error:", error);
    }
});