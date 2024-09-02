
import React from 'react';
import { Box, TextField, MenuItem, Typography, Select, InputLabel, FormControl } from '@mui/material';

const genderOptions = ['Male', 'Female', 'Non-binary'];

const PersonalInfo: React.FC = () => {
    const [formData, setFormData] = React.useState({
      name: '',
      gender: '',
      age: '',
    });
  
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      setFormData({
        ...formData,
        [event.target.name]: event.target.value,
      });
    };
  
    return (
      <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh">
        <Typography variant="h4">Personal Information</Typography>
        <TextField 
            id="outlined-basic" 
            label="Full Name" 
            name="name" 
            variant="outlined" 
            value={formData.name}
            onChange={handleChange}   
            sx={{ marginBottom: '1rem' }}
        />

        <FormControl sx={{ width: '220px', marginBottom: '1rem' }}>
          <InputLabel id="demo-simple-select-label">Gender</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={formData.gender}
            label="Gender"
            // onChange={handleChange}
          >
            <MenuItem value={"male"}>Male</MenuItem>
            <MenuItem value={"female"}>Female</MenuItem>
            <MenuItem value={"non_binary"}>non-Binary</MenuItem>
          </Select>
        </FormControl>
        <TextField 
            id="outlined-basic" 
            label="Age" 
            name="age" 
            variant="outlined" 
            value={formData.age}
            onChange={handleChange}    
        />
      </Box>
    );
  };

export default PersonalInfo;