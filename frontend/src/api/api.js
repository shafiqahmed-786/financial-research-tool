import axios from "axios";

const API_BASE =
  process.env.REACT_APP_API_URL ||
  "https://financial-research-tool-g1ni.onrender.com/api";

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
