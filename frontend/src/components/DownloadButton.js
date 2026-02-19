import { downloadExcel } from "../api/api";

function DownloadButton({ fileId }) {
  const handleDownload = () => {
    window.open(downloadExcel(fileId), "_blank");
  };

  return (
    <button onClick={handleDownload}>
      Download Excel
    </button>
  );
}

export default DownloadButton;
