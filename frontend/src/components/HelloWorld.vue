<template>
  <div>
    <h1 class="title">Team Optimization</h1>
    <form @submit.prevent="submitRequirements" class="form">
      <label for="requirements" class="label">Enter project requirements:</label><br>
      <textarea v-model="requirements" id="requirements" name="requirements" rows="4" cols="50" class="textarea"></textarea><br>
      <button type="submit" class="button">Submit</button>
    </form>
    <div v-if="response" class="response-box">{{ response.choices[0].message.content }}</div>
    <br>
    <br>
    <div class="users">
      <div v-for="user in users.developers" :key="user.id" class="user-card">
        <h2 class="user-name">{{ user.name }}</h2>
        <p class="user-info">Tech Stack: {{ user.tech_stack }}</p>
        <p class="user-info">Experience: {{ user.experience }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      requirements: '',
      response: '',
      users: []
    };
  },
  methods: {
    async submitRequirements() {
      try {
        const response = await axios.post('http://localhost:5000/suggest_team', { requirements: this.requirements });
        this.response = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async fetchUsers() {
      try {
        const response = await axios.get('http://localhost:5000/developers');
        this.users = response.data;
      } catch (error) {
        console.error(error);
      }
    }
  },
  mounted() {
    this.fetchUsers();
  }
};
</script>

<style>
.title {
  text-align: center;
  color: #333;
  margin-bottom: 20px;
}

.form {
  margin-bottom: 20px;
}

.label {
  font-size: 18px;
}

.textarea {
  width: 60%;
  padding: 5px;
  font-size: 16px;
  margin-bottom: 10px;
}

.response-box {
  border: 2px solid #4CAF50; 
  background-color: #f9f9f9; 
  padding: 20px;
  margin-top: 20px; 
  border-radius: 5px; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
  font-size: 18px; 
  line-height: 1.6; 
  text-align: center; 
}

.button {
  padding: 5px 10px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}

.button:hover {
  background-color: #0056b3;
}

.response {
  margin-bottom: 20px;
}

.users {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.user-card {
  width: calc(33.33% - 20px);
  margin-right: 20px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.user-name {
  font-size: 18px;
  margin-bottom: 5px;
}

.user-info {
  font-size: 14px;
  margin-bottom: 5px;
}

@media (max-width: 768px) {
  .user-card {
    width: 100%;
    margin-right: 0;
  }
}
</style>
