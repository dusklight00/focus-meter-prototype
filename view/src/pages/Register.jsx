import React from "react";
import {
  Container,
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Stack,
  MenuItem,
} from "@mui/material";

const currencies = [
  {
    value: "USD",
    label: "$",
  },
  {
    value: "EUR",
    label: "€",
  },
  {
    value: "BTC",
    label: "฿",
  },
  {
    value: "JPY",
    label: "¥",
  },
];

function Register() {
  return (
    <Container className="h-[100vh] flex place-content-center" maxWidth="sm">
      <Card>
        <CardContent>
          <Stack gap={3}>
            <Typography variant="h5">
              <b>Register</b>
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
            <TextField
              id="outlined-select-currency"
              select
              label="Type"
              defaultValue="teacher"
              // helperText="Please select your currency"
            >
              <MenuItem key="teacher" value="teacher">
                Teacher
              </MenuItem>
              <MenuItem key="student" value="student">
                Student
              </MenuItem>
            </TextField>
            <Button variant="contained">Register</Button>
          </Stack>
        </CardContent>
      </Card>
    </Container>
  );
}

export default Register;
