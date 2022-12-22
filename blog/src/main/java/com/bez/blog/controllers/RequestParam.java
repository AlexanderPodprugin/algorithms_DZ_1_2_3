package com.bez.blog.controllers;

public @interface RequestParam {
    String defaultValue();

    boolean required();

    String name();
}
