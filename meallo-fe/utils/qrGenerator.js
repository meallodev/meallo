"use client"
import React from "react";
import { QRCodeCanvas } from "qrcode.react";
import { useNavigate } from "react-router-dom";

const QRCodeGenerator = ({ url }) => {
//   const navigate = useNavigate();

  const handleRedirect = () => {
    // navigate(url);
    console.log("clicked")
  };

  return (
    <div style={{ textAlign: "center" }}>
      <h2>Scan this QR Code</h2>
      <QRCodeCanvas value={window.location.origin + url} size={200} />
      <br />
      <button onClick={handleRedirect} style={{ marginTop: "20px" }}>
        Go to Page
      </button>
    </div>
  );
};

export default QRCodeGenerator;
