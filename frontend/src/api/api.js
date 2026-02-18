import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/api",
});

export const uploadFile = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return API.post("/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};

export const extractData = (fileId) => {
  return API.post(`/extract/${fileId}`);
};

export const downloadExcel = (fileId) => {
  return `${API.defaults.baseURL}/download/${fileId}`;
};
