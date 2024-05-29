import Webcam from "react-webcam";
import {
  Container,
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Stack,
} from "@mui/material";

function App() {
  return (
    <Container
      className="h-[100vh] flex place-content-center border"
      maxWidth="sm"
    >
      <Card>
        <CardContent>
          <Stack gap={3}>
            <Typography variant="h5">
              <b>Login</b>
            </Typography>
            <TextField
              label="Username"
              variant="outlined"
              // onChange={(e) => setUsername(e.target.value)}
            />
            <TextField
              label="Password"
              variant="outlined"
              // onChange={(e) => setPassword(e.target.value)}
            />
            <Button variant="contained">Login</Button>
          </Stack>
        </CardContent>
      </Card>
    </Container>
  );
}

export default App;
