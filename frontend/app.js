const inputText = document.getElementById("inputText");
const answerBox = document.getElementById("answer");


async function sendRequest(url) {

    const text = inputText.value.trim();


    if (text === "") {

        answerBox.innerText =
            "Please enter something first.";

        return;

    }


    answerBox.innerText =
        "Thinking...";


    try {

        const response = await fetch(url, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })

        });


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail || "Server error"
            );

        }


        answerBox.innerText =
            data.answer || "No answer received.";


    } catch (error) {

        console.error(error);

        answerBox.innerText =
            "Unable to get answer: " + error.message;

    }

}


/* Ask Question */

function askQuestion() {

    sendRequest("/ask");

}


/* Simplify Concept */

function simplifyConcept() {

    sendRequest("/simplify");

}


/* Generate Quiz */

function generateQuiz() {

    sendRequest("/quiz");

}


/* Learning Path */

function generateLearningPath() {

    sendRequest("/learning-path");

}


/* Summarize */

function summarizeText() {

    sendRequest("/summarize");

}