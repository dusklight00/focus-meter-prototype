import React from "react";

import {
  AppBar,
  Toolbar,
  IconButton,
  // MenuIcon,
  Box,
  Fab,
  Card,
  CardContent,
  CardActions,
  Grid,
  // Item,
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

function Room() {
  return (
    <div>
      <Grid container spacing={2} padding={2}>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
      </Grid>
      <Grid container spacing={2} padding={2}>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
      </Grid>
      <Grid container spacing={2} padding={2}>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
        <Grid item xs={3}>
          <Card>
            <CardContent>asd</CardContent>
          </Card>
        </Grid>
      </Grid>
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
    </div>
  );
}

export default Room;
