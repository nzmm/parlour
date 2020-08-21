function queryString(params: any): string {
    return new URLSearchParams(params).toString()
}

function getCookie(name: string) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    return parts.length === 2 ? parts[1].split(";")[0] : "";
}

function withCRSF(config: any, csrftoken: string = "csrftoken") {
    const headers = {...config.headers, 'X-CSRFToken': getCookie(csrftoken)};
    return {...config, headers};
}

export async function GET(url: string, params?: any) {
    const getUrl = params ? `${url}?${queryString(params)}` : url;
    return fetch(getUrl)
        .then(response => {
            return response;
        })
        .catch(error => {
            console.error(error);
            return error;
        });
}

export async function POST(url: string, data?: any) {
    const config = withCRSF({
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    return fetch(url, config)
        .then(response => {
            return response;
        })
        .catch(error => {
            console.error(error);
            return error;
        });
}
