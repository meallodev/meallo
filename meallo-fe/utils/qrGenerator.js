"use client";
import { QRCodeCanvas } from "qrcode.react";
import { useRouter } from "next/navigation";

export default function QRCodeGenerator() {
  const router = useRouter();
  const formURL = `${window.location.origin}/form`; // Next.js route

  const handleRedirect = () => {
    router.push("/form");
  };

  return (
    <div className="flex flex-col items-center mt-10">
      <h2 className="text-2xl font-bold">Scan this QR Code</h2>
      <QRCodeCanvas value={formURL} size={200} className="mt-4" />
      <button
        onClick={handleRedirect}
        className="mt-4 bg-blue-500 text-white p-2 rounded"
      >
        Go to Form
      </button>
    </div>
  );
}
