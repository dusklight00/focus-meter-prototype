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
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);
  return (
    <div>
      <Button>Create Room</Button>
      <Button onClick={handleOpen}>Open modal</Button>
      <Modal
        aria-labelledby="transition-modal-title"
        aria-describedby="transition-modal-description"
        open={open}
        onClose={handleClose}
        closeAfterTransition
        slots={{ backdrop: Backdrop }}
        slotProps={{
          backdrop: {
            timeout: 500,
          },
        }}
      >
        <Fade in={open}>
          <Box sx={style}>
            <Typography id="transition-modal-title" variant="h6" component="h2">
              Text in a modal
            </Typography>
            <Typography id="transition-modal-description" sx={{ mt: 2 }}>
              Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
            </Typography>
          </Box>
        </Fade>
      </Modal>
    </div>
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
