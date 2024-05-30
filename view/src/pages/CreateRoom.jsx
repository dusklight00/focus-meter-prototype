import React from "react";

import {
  Container,
  Button,
  Card,
  Stack,
  CardContent,
  Typography,
} from "@mui/material";

function RoomComponent() {
  return (
    <Card sx={{ p: 2 }}>
      <Typography variant="h5" component="div">
        Mathematics
      </Typography>
      <Typography sx={{ mb: 1.5 }} color="text.secondary">
        ijk-acb-klm
      </Typography>
      <Stack gap="10px" direction="row">
        <Button variant="outlined" size="small">
          Join
        </Button>
        <Button variant="outlined" size="small">
          Delete
        </Button>
      </Stack>
    </Card>
  );
}

function CreateRoom() {
  return (
    <div>
      <Container maxWidth="sm">
        <Stack gap="10px" sx={{ pt: 2, pb: 2 }}>
          <Button>Create Room</Button>
          <Button>Join Room</Button>
          <RoomComponent />
        </Stack>
      </Container>
    </div>
  );
}

export default CreateRoom;
