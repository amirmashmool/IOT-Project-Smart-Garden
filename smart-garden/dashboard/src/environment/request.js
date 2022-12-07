import axios from "axios";

export default () => {
  const request = axios.create({
    baseURL: "http://localhost:3000/api",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });

  return request;
};
