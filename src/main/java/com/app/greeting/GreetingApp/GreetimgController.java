package com.app.greeting.GreetingApp;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetimgController {
	
	@RequestMapping("/getGreeting")
	public String getGreeting() {
		
		return "Hello AWS_CICD_Pipelines";
	}

}
