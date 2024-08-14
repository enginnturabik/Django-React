import axios from 'axios';

const API_URL = 'http://localhost:8000/api/auth/';

const register = (username, email, password, role) => {
  return axios.post(API_URL + 'signup/', {
    username,
    email,
    password,
    role,
  });
};

const login = (username, password) => {
  return axios.post(API_URL + 'login/', {
    username,
    password,
  }).then(response => {
    if (response.data.access) {
      localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
  });
};

const logout = () => {
  localStorage.removeItem('user');
};

export default {
  register,
  login,
  logout,
};
