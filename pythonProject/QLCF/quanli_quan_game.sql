create database quanli_quan_game;

use quanli_quan_game;
-- Tạo bảng "Menu"
CREATE TABLE Menu (
    MenuID INT PRIMARY KEY,
    TenMenu VARCHAR(255),
    BieuTuong VARCHAR(255)
);

-- Tạo bảng "NhanVien"
CREATE TABLE NhanVien (
    IDNhanVien INT PRIMARY KEY,
    TenNhanVien VARCHAR(255),
    VaiTro VARCHAR(50)
);

-- Tạo bảng "KhachHang"
CREATE TABLE KhachHang (
    IDKhachHang INT PRIMARY KEY,
    TenKhachHang VARCHAR(255)
);

-- Tạo bảng "DichVu"
CREATE TABLE DichVu (
    IDDichVu INT PRIMARY KEY,
    TenDichVu VARCHAR(255)
);
CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);
-- Create the member table
CREATE TABLE member (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);