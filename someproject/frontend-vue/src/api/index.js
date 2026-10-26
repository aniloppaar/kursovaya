import axios from 'axios';

export const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  headers: { 'Content-Type': 'application/json' },
});

export const getTours = (params = {}) => api.get('/tours/', { params });
export const getTourById = (id) => api.get(`/tours/${id}/`);
export const createBooking = (data) => api.post('/bookings/', data);