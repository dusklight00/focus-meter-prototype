import Webcam from "react-webcam";
import Login from "./pages/Login.jsx";
import Register from "./pages/Register.jsx";

import {
  AppBar,
  Toolbar,
  IconButton,
  // MenuIcon,
  Box,
  Fab,
  // SearchIcon,
  // MoreIcon,
} from "@mui/material";

import AddIcon from "@mui/icons-material/Add";
import SearchIcon from "@mui/icons-material/Search";
import MoreIcon from "@mui/icons-material/More";
import { styled } from "@mui/material/styles";
import MenuIcon from "@mui/icons-material/Menu";
import CallEndIcon from "@mui/icons-material/CallEnd";
import MicIcon from "@mui/icons-material/Mic";
import HeadphonesIcon from "@mui/icons-material/Headphones";
import VideocamIcon from "@mui/icons-material/Videocam";

const StyledFab = styled(Fab)({
  position: "absolute",
  zIndex: 1,
  top: -30,
  left: 0,
  right: 0,
  margin: "0 auto",
});

function App() {
  return (
    <>
      <AppBar position="fixed" color="primary" sx={{ top: "auto", bottom: 0 }}>
        <Toolbar>
          <IconButton color="inherit" aria-label="open drawer">
            <HeadphonesIcon />
          </IconButton>
          <IconButton color="inherit" aria-label="open drawer">
            <VideocamIcon />
          </IconButton>
          <IconButton color="inherit" aria-label="open drawer">
            <MicIcon />
          </IconButton>
          <StyledFab color="secondary" aria-label="add">
            <CallEndIcon />
          </StyledFab>
          <Box sx={{ flexGrow: 1 }} />
          {/* <IconButton color="inherit">
            <SearchIcon />
          </IconButton>
          <IconButton color="inherit">
            <MoreIcon />
          </IconButton> */}
        </Toolbar>
      </AppBar>
    </>
  );
}

export default App;
