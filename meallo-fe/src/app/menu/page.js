"use client";
import { useEffect, useState } from "react";
import Image from "next/image";

export default function MenuPage() {
    const [menu, setMenu] = useState([]);

    useEffect(() => {
        const fetchMenu = async () => {
            const res = await fetch("http://localhost:8000/get-menu");
            const data = await res.json();
            console.log(data);
            setMenu(data.menu || []);
        };
        fetchMenu();
    }, []);
 
    return (
        <div className="min-h-screen bg-gray-100 p-6">
            <h1 className="text-3xl font-bold text-center text-gray-800 mb-6">Restaurant Menu</h1>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {menu.map((item, index) => (
                     <div key={`${item.id}-${index}`} className="bg-white p-4 rounded-lg shadow-md hover:shadow-lg transition">
                        <Image src={item.image} alt={item.name} height={50} width={100} className="w-full h-40 object-cover rounded-md mb-4" />
                        <h2 className="text-xl font-semibold text-gray-900">{item.name}</h2>
                        <p className="text-gray-600 text-lg">${item.price.toFixed(2)}</p>
                        <button className="mt-4 w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition">
                            Add to Cart
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}
