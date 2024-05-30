import Webcam from "react-webcam";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";
import Room from "./pages/Room.jsx";
import instance from "../instance.js";

import { useRef, useEffect } from "react";

function App() {
  const webRef = useRef(null);

  const showImage = () => {
    console.log(webRef.current.getScreenshot());
  };

  const FPS = 100;

  useEffect(() => {
    const interval = setInterval(() => {
      console.log(webRef.current.getScreenshot());
      instance
        .get("/get_feed?image_base64=" + webRef.current.getScreenshot())
        .then((res) => {
          console.log(res.data);
        });
    }, 1000 / FPS);
    return () => clearInterval(interval);
  });

  return (
    <>
      <Webcam ref={webRef} />
      <button
        onClick={() => {
          showImage();
        }}
      >
        Show image in console
      </button>
      {/* <Room /> */}
    </>
  );
}

export default App;
