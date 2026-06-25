from .database import get_connection


class ProfileManager:
    def create_profile(self, username, display_name="", bio="", status="", avatar_path=""):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("""
                INSERT INTO profiles 
                (username, display_name, bio, status, avatar_path)
                VALUES (?, ?, ?, ?, ?)
            """, (username, display_name, bio, status, avatar_path))

            conn.commit()
            return True

        except Exception as error:
            print("Create profile error:", error)
            return False

        finally:
            conn.close()

    def get_profile(self, username):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT username, display_name, bio, status, avatar_path
            FROM profiles
            WHERE username = ?
        """, (username,))

        result = cursor.fetchone()
        conn.close()

        if not result:
            return None

        return {
            "username": result[0],
            "display_name": result[1],
            "bio": result[2],
            "status": result[3],
            "avatar_path": result[4]
        }

    def update_profile(self, username, display_name, bio, status, avatar_path):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE profiles
            SET display_name = ?, bio = ?, status = ?, avatar_path = ?
            WHERE username = ?
        """, (display_name, bio, status, avatar_path, username))

        conn.commit()
        conn.close()

    def delete_profile(self, username):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM profiles
            WHERE username = ?
        """, (username,))

        conn.commit()
        conn.close()
