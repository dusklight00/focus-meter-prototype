import Webcam from "react-webcam";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";
import Room from "./pages/Room.jsx";

import { useRef } from "react";

function App() {
  const webRef = useRef(null);

  const showImage = () => {
    console.log(webRef.current.getScreenshot());
  };

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
