import axios from "axios";

/*
  In production (Vercel), this will use:
  REACT_APP_API_URL

  Locally, it will fall back to:
  http://127.0.0.1:5000/api
*/

const API_BASE =
  process.env.REACT_APP_API_URL || "http://127.0.0.1:5000/api";

const API = axios.create({
  baseURL: API_BASE,
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
  return `${API_BASE}/download/${fileId}`;
};
