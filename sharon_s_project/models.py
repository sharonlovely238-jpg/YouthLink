from datetime import datetime, timezone

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    student_id: Mapped[str | None] = mapped_column(String(50), unique=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)


class Petition(Base):
    __tablename__ = "petitions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False, default="Untitled Petition")
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    comments: Mapped[list["PetitionComment"]] = relationship(
        back_populates="petition",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    votes: Mapped[list["PetitionVote"]] = relationship(
        back_populates="petition",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
    signatures: Mapped[list["PetitionSignature"]] = relationship(
        back_populates="petition",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class PetitionComment(Base):
    __tablename__ = "petition_comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    petition_id: Mapped[int] = mapped_column(
        ForeignKey("petitions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    petition: Mapped[Petition] = relationship(back_populates="comments")


class PetitionVote(Base):
    __tablename__ = "petition_votes"
    __table_args__ = (
        UniqueConstraint("petition_id", "username", name="uq_petition_vote_user"),
        CheckConstraint("value IN (-1, 1)", name="ck_petition_vote_value"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    petition_id: Mapped[int] = mapped_column(
        ForeignKey("petitions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    petition: Mapped[Petition] = relationship(back_populates="votes")


class PetitionSignature(Base):
    __tablename__ = "petition_signatures"
    __table_args__ = (
        UniqueConstraint("petition_id", "username", name="uq_petition_signature_user"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    petition_id: Mapped[int] = mapped_column(
        ForeignKey("petitions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    petition: Mapped[Petition] = relationship(back_populates="signatures")


class DiscussionThread(Base):
    __tablename__ = "discussion_threads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    comments: Mapped[list["ThreadComment"]] = relationship(
        back_populates="thread",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class ThreadComment(Base):
    __tablename__ = "thread_comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    thread_id: Mapped[int] = mapped_column(
        ForeignKey("discussion_threads.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    thread: Mapped[DiscussionThread] = relationship(back_populates="comments")

class Opportunity(Base):
    __tablename__ = "opportunities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    organization: Mapped[str] = mapped_column(String(150), nullable=False)
    deadline: Mapped[str | None] = mapped_column(String(50), nullable=True)
    link: Mapped[str | None] = mapped_column(String(500), nullable=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    comments: Mapped[list["OpportunityComment"]] = relationship(
        back_populates="opportunity",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class OpportunityComment(Base):
    __tablename__ = "opportunity_comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    opportunity_id: Mapped[int] = mapped_column(
        ForeignKey("opportunities.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)

    opportunity: Mapped[Opportunity] = relationship(back_populates="comments")