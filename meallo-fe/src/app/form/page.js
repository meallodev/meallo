"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function FormPage() {
    const [contactNumber, setContactNumber] = useState("");
    const [name, setName] = useState("");
    const [otpSent, setOtpSent] = useState(false);
    const [otp, setOtp] = useState("");
    const router = useRouter();

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        // Call addCustomer API
        const addCustomerResponse = await fetch("http://localhost:8000/addCustomer/", {
            method: "POST",
            body: JSON.stringify({ name, contactNumber }),
            headers: { "Content-Type": "application/json" },
        });
    
        if (!addCustomerResponse.ok) {
            alert("Error adding customer!");
            return;
        }
    
        // Call submit-form API to send OTP
        const otpResponse = await fetch("http://localhost:8000/submit-form", {
            method: "POST",
            body: JSON.stringify({ name, contactNumber }),
            headers: { "Content-Type": "application/json" },
        });
    
        if (otpResponse.ok) {
            setOtpSent(true);
        } else {
            alert("Error sending OTP!");
        }
    };    

    const handleVerify = async (e) => {
        e.preventDefault();
        const response = await fetch("http://localhost:8000/verify-otp", {
            method: "POST",
            body: JSON.stringify({ contactNumber, otp }),
            headers: { "Content-Type": "application/json" },
        });
        if (response.ok) router.push("/menu");
    };

    return (
        <div>
            {!otpSent ? (
                <form onSubmit={handleSubmit}>
                    <input type="text" placeholder="Name" onChange={(e) => setName(e.target.value)} required />
                    <input type="text" placeholder="contactNumber" onChange={(e) => setContactNumber(e.target.value)} required />
                    <button type="submit">Submit</button>
                </form>
            ) : (
                <form onSubmit={handleVerify}>
                    <input type="text" placeholder="Enter OTP" onChange={(e) => setOtp(e.target.value)} required />
                    <button type="submit">Verify</button>
                </form>
            )}
        </div>
    );
}
