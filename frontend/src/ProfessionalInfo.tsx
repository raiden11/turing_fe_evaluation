


import React from 'react';
import { Box, TextField, MenuItem, Typography, Select, Chip, InputLabel, FormControl, OutlinedInput } from '@mui/material';

const professions = ['Owner', 'Agent', 'Buyer', 'Seller'];
const skills = ['JavaScript', 'React', 'Node.js', 'Python'];

const ProfessionalInfo: React.FC = () => {
    const [formData, setFormData] = React.useState({
        profession: '',
        skills: [],
        services: '',
    });
  
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      setFormData({
        ...formData,
        [event.target.name]: event.target.value,
      });
    };

    const handleSkillsChange = (event: any) => {
        setFormData({
            ...formData,
            skills: event.target.value,
    });
    };
  
    return (
        <Box display="flex" flexDirection="column" alignItems="center" justifyContent="center" height="100vh">
            <Typography variant="h4">Professional Information</Typography>
            <TextField
                select
                sx={{ marginBottom: '1rem', width: '220px' }}
                label="Profession"
                name="profession"
                value={formData.profession}
                onChange={handleChange}
                margin="normal"
                variant="outlined"
            >
                {professions.map((option) => (
                <MenuItem key={option} value={option}>
                    {option}
                </MenuItem>
                ))}
            </TextField>
            <FormControl fullWidth margin="normal" variant="outlined">
                <InputLabel>Skills</InputLabel>
                <Select
                multiple
                sx={{ marginBottom: '1rem', width: '220px' }}
                value={formData.skills}
                onChange={handleSkillsChange}
                input={<OutlinedInput label="Skills" />}
                renderValue={(selected) => (
                    <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                    {selected.map((value) => (
                        <Chip key={value} label={value} />
                    ))}
                    </Box>
                )}
                >
                {skills.map((option) => (
                    <MenuItem key={option} value={option}>
                    {option}
                    </MenuItem>
                ))}
                </Select>
            </FormControl>
            <TextField 
                id="outlined-basic" 
                label="Services" 
                name="services" 
                variant="outlined" 
                value={formData.services}
                onChange={handleChange}    
            />
        </Box>
    );
  };

export default ProfessionalInfo;