const utf8ToB64 = (str) => {
    const utf8Bytes = new TextEncoder().encode(str);
    let binary = "";
    utf8Bytes.forEach((b) => (binary += String.fromCharCode(b)));
    return btoa(binary);
  };

export async function fetchExpenses(url, username, password) {
  const credentials = utf8ToB64(`${username}:${password}`);
  const res = await fetch(
        url,
        {
          headers: {
            Authorization: `Basic ${credentials}`,
          },
        },
      );
  
  if (res.status === 401) {
    throw new Error("Unauthorized")
  }

  return await res.json()
}
