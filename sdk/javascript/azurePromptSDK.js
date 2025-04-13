import axios from "axios";

class AzurePromptSDK {
    constructor(baseURL = "https://prompt-validator.azurewebsites.net") {
        this.baseURL = baseURL;
    }

    async validatePrompt(prompt) {
        const response = await axios.post(`${this.baseURL}/validate`, { prompt });
        return response.data;
    }
}

export default AzurePromptSDK;