import axios from 'axios';

const apiInstance = axios.create({
  baseURL: 'http://localhost:3000/api', 
});

class ApiRepository {
  constructor(endpoint) {
    this.endpoint = endpoint;
  }

  async getAll() {
    try {
      const response = await apiInstance.get(`/${this.endpoint}`);
      return response.data;
    } catch (error) {
      this.handleApiError(error);
    }
  }

  async create(newData) {
    try {
      const response = await apiInstance.post(`/${this.endpoint}`, newData);
      return response.data;
    } catch (error) {
      this.handleApiError(error);
    }
  }
  
  async getAll() {
    try {
      const response = await apiInstance.get(`/${this.endpoint}`);
      return response.data;
    } catch (error) {
      this.handleApiError(error);
    }
  }


  // Other CRUD methods...

  handleApiError(error) {
    console.error(`API Error in ${this.endpoint}:`, error);
    throw error;
  }
}

// api/RoomsApi.js
class RoomsApi {
  constructor(axiosInstance) {
    this.axios = axiosInstance;
  }

  async getAllRooms() {
    // ...
  }

  async getAvailableRooms(startDate, endDate) {
    // ...
  }

  // Other room-related methods...
}

// api/GuestsApi.js
class GuestsApi {
  constructor(axiosInstance) {
    this.axios = axiosInstance;
  }

  async getAllGuests() {
    // ...
  }

  async getGuestReservations(guestId) {
    // ...
  }

  // Other guest-related methods...
}

// api/ReservationsApi.js
class ReservationsApi {
  constructor(axiosInstance) {
    this.axios = axiosInstance;
  }

  async getAllReservations() {
    // ...
  }

  async createReservation(newReservationData) {
    // ...
  }

  // Other reservation-related methods...
}

export default ApiRepository;