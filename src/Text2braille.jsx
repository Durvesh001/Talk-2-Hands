import React, { useState } from "react";
import Navbar from "./components/Navbar";
import "./Text2braille.css";

const Text2braille = () => {
    const [inputText, setInputText] = useState("");
    const [result, setResult] = useState("");

    const handleInputChange = (event) => {
        setInputText(event.target.value); // Update the state with the input value
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch("http://localhost:5000/braille", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ text: inputText }), // Send the entered text as JSON data
            });

            if (response.ok) {
                // Request was successful, handle response from Flask server if needed
                const data = await response.json();
                setResult(data);
                console.log("Response from server:", data);

                // // Clear the input field after successful submission
                // setInputText(""); // Reset inputText state to an empty string
            } else {
                // Handle errors if the request was not successful
                console.error("Error:", response.statusText);
            }
        } catch (error) {
            console.error("Error:", error);
        }
    };

    return (
        <>
            <Navbar />
            <div className="main">
                <h1 className="brailleh1">Text-to-Braille</h1>
                <h3>Enter the text to be converted - </h3>
                <form onSubmit={handleSubmit}>
                    <textarea
                        value={inputText}
                        onChange={handleInputChange}
                        rows="200"
                        cols="90"
                    />
                    <br />
                    <div className="submit">
                        <button type="submit" className="Submit">Submit</button>
                    </div>
                </form>
                <div className="brailleOutput">
                    <h3 className="textout">Braille Output - </h3>
                    <p className="result">{result}</p>
                </div>
            </div>
        </>
    );
};

export default Text2braille;
