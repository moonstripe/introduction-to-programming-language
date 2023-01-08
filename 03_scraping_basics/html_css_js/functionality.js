
// Newsletter functionality

const submitNewsletter = () => {
    let name = document.querySelector("#newsletter-name")
    let email = document.querySelector("#newsletter-email")

    console.log(`subscribing ${name.value} with email: ${email.value} to the newsletter`)
}

document.querySelector("#submit").addEventListener('click', submitNewsletter)

// Adding a paragraph

const textContent = document.querySelector("#text-content")

const newDiv = document.createElement('div')
newDiv.className = "main-content"

const newText = document.createElement('p')
newText.innerText = "Lorem text is super boring, but helps typographers set text."
newText.id = "paragraph-3"

const newHeader = document.createElement('h4')
newHeader.innerText = "Mysterious Header"

newDiv.appendChild(newHeader)
newDiv.appendChild(newText)
textContent.appendChild(newDiv)
