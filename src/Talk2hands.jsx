import React, { useState, useEffect, useRef } from "react";
import './Talk2hands.css'
import Navbar from "./components/Navbar";

const Talk2hands = () => {
    const canvasRef = useRef();
    const imageRef = useRef();
    const videoRef = useRef();
    const [result, setResult] = useState("");

    // Getting the video access and keeping the audio as False
    useEffect(() => {
        async function getCameraStream() {
            const stream = await navigator.mediaDevices.getUserMedia({
                audio: false,
                video: true,
            });

            if (videoRef.current) {
                videoRef.current.srcObject = stream;
            }
        };

        getCameraStream();
    }, []);



    // Caputre image with 30 fps and POST it to the 'classify' function at 'http://localhost:5000/classify'.
    // If then the response if 200 i.e. its indicating success, the response is converted to text form 
    // and 'result' variable is set to response value.
    useEffect(() => {
        const interval = setInterval(async () => {
            captureImageFromCamera();

            if (imageRef.current) {
                const formData = new FormData();
                formData.append('image', imageRef.current);

                const response = await fetch('http://localhost:5000/classify', {
                    method: "POST",
                    body: formData,
                });

                if (response.status === 200) {
                    const text = await response.text();
                    setResult(text);
                } else {
                    setResult("Error from API.");
                }
            }
        }, 33.3333);
        return () => clearInterval(interval);
    }, []);

    const playCameraStream = () => {
        if (videoRef.current) {
            videoRef.current.play();
        }
    };


    // Captures the image
    const captureImageFromCamera = () => {
        const context = canvasRef.current.getContext('2d');
        const { videoWidth, videoHeight } = videoRef.current;

        canvasRef.current.width = videoWidth;
        canvasRef.current.height = videoHeight;

        context.drawImage(videoRef.current, 0, 0, videoWidth, videoHeight);

        canvasRef.current.toBlob((blob) => {
            imageRef.current = blob;
        })
    };



    return (

        <>
            <Navbar />
            <div className="body-prediction">
                <header>
                    <h1>Text-to-Speech</h1>
                </header>

                <main>
                    <div className="videoElement">
                        <video ref={videoRef} onCanPlay={() => playCameraStream()} id="video" />
                    </div>
                    <canvas ref={canvasRef} hidden></canvas>
                    <p className="output-prediction">Predicted Output: {result}</p>
                </main>
            </div>
        </>
    );
};

export default Talk2hands;
